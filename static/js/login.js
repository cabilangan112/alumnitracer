        var g_urls = {
            'login': '{% url "rest_login" %}',
            'logout': '{% url "rest_logout" %}',
 
        };
        var g_auth = localStorage.getItem("auth");
        if(g_auth == null) {
            g_auth = sessionStorage.getItem("auth");
        }
        
        if(g_auth) {
            try {
                g_auth = JSON.parse(g_auth);
            } catch(error) {
                g_auth = null; 
            }
        }

        var getCookie = function(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        };
        var g_csrftoken = getCookie('csrftoken');

        var initLogin = function() {
            if(g_auth) {
                $('#non-logged-in').hide();
                $('#logged-in').show();
                $('#span-username').html(g_auth.username);
                if(g_auth.remember_me) {
                    localStorage.setItem("auth", JSON.stringify(g_auth));
                } else {
                    sessionStorage.setItem("auth", JSON.stringify(g_auth));
                }
            } else {
                $('#non-logged-in').show();
                $('#logged-in').hide();
                $('#span-username').html('');
                localStorage.removeItem("auth");
                sessionStorage.removeItem("auth");
            }
            $('#test-auth-response').html("");
        };

        $(function () {
            initLogin(); 

            $('#loginButton').click(function() {
                $('#login-modal').addClass('active');
            });
            
            $('.close-modal').click(function() {
                $('#login-modal').removeClass('active');
            });
 
            
            $('#loginOkButton').click(function() {
                var username = $('#input-username').val();
                var password = $('#input-password').val();
                var remember_me = $('#input-local-storage').prop('checked');
                if(username && password) {
                    console.log("Will try to login with ", username, password);
                    $('#modal-error').addClass('d-invisible');
                    $.ajax({
                        url: g_urls.login, 
                        method: "POST", 
                        data: {
                            username: username,
                            password: password,
                            csrfmiddlewaretoken: g_csrftoken
                        }
                    }).done(function(data) {
                        console.log("DONE: ", username, data.key);
                        g_auth = {
                            username: username,
                            key: data.key,
                            remember_me: remember_me
                        };
                        $('#login-modal').removeClass('active');
                        initLogin();
                        // CAREFUL! csrf token is rotated after login: https://docs.djangoproject.com/en/1.7/releases/1.5.2/#bugfixes
                        g_csrftoken = getCookie('csrftoken');
                    }).fail(function(data) {
                        console.log("FAIL", data);
                        $('#modal-error').removeClass('d-invisible');
                    });
                } else {
                    $('#modal-error').removeClass('d-invisible');
                }
            });

            $('#logoutButton').click(function() {
                console.log("Trying to logout");
                $.ajax({
                    url: g_urls.logout, 
                    method: "POST", 
                    beforeSend: function(request) {
                        request.setRequestHeader("Authorization", "Token " + g_auth.key);
                    },
                    data: {
                        csrfmiddlewaretoken: g_csrftoken
                    }
                }).done(function(data) {
                    console.log("DONE: ", data);
                    g_auth = null;
                    initLogin();
                }).fail(function(data) {
                    console.log("FAIL: ", data);
                });
            });
            

        });
        