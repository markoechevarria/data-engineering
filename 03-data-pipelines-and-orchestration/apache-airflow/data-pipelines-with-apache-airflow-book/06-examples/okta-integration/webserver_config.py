"""Default configuration for the Airflow webserver."""

from __future__ import annotations
import os
from flask_appbuilder.const import AUTH_DB


basedir = os.path.abspath(os.path.dirname(__file__))


WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None


from flask_appbuilder.security.manager import AUTH_OAUTH
from airflow.www.security import AirflowSecurityManager

AUTH_TYPE = AUTH_OAUTH

AUTH_USER_REGISTRATION = True

AUTH_ROLES_SYNC_AT_LOGIN = True

AUTH_ROLES_MAPPING = {
    "airflow_admins": ["Admin"],
    "airflow_users": ["User"],
    "airflow_viewers": ["Viewer"],
    "airflow_lions": ["Lions"],
    "airflow_zebras": ["Zebras"]
}

class OktaSecurityManager(AirflowSecurityManager):

    def oauth_user_info(self, provider, response=None):

        if provider == "okta":

            me = self.appbuilder.sm.oauth_remotes[provider].get(
                "https://integrator-1588976.okta.com/oauth2/default/v1/userinfo"
            )

            return {
                "username": data.get("preferred_username"),
                "email": data.get("email"),
                "first_name": data.get("given_name", ""),
                "last_name": data.get("family_name", ""),
                "role_keys": data.get("groups", [])
            }

SECURITY_MANAGER_CLASS = OktaSecurityManager
OAUTH_PROVIDERS = [
    {
        "name": "okta",
        "token_key": "access_token",
        "icon": "fa-okta",
        "remote_app": {
            "client_id": "CLIENT_ID_KEY",
            "client_secret": "CLIENT_SECRET_KEY"
            "api_base_url": "https://integrator-1588976.okta.com/oauth2/default",
            "access_token_url": "https://integrator-1588976.okta.com/oauth2/default/v1/token",
            "authorize_url": "https://integrator-1588976.okta.com/oauth2/default/v1/authorize",
            "server_metadata_url": "https://integrator-1588976.okta.com/oauth2/default/.well-known/openid-configuration",
            "client_kwargs": {
                "scope": "openid profile email groups"
            },
        },
    }
]
