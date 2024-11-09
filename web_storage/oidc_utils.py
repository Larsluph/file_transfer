from flask import session, g

def require_admin(func):
    def wrapper(*args, **kwargs):
        current_user_groups = session["oidc_auth_profile"].get("groups")
        admin_user_groups = { "authentik Admins" }
        if not set(current_user_groups).intersection(admin_user_groups):
            return "You are not authorized to access this page", 403
        return func(*args, **kwargs)
    return wrapper
