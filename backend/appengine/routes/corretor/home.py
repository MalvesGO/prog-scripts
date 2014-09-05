# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from permission_app.model import CORRETOR
from tekton import router
from routes.login import passwordless, facebook


@permissions(CORRETOR)
@no_csrf
def index():
    return TemplateResponse({'passwordless_admin_path': router.to_path(passwordless.form),
                             'facebook_admin_path': router.to_path(facebook.form)})
