# MIT License
#
# Copyright The SCons Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
Common functions for Microsoft Visual Studio and Visual C/C++.
"""


import SCons.Errors
import SCons.Platform.win32
import SCons.Util

from SCons.Tool.MSCommon.sdk import mssdk_exists, mssdk_setup_env

from SCons.Tool.MSCommon.vc import (
    msvc_exists,
    msvc_setup_env_tool,
    msvc_setup_env_once,
    msvc_version_to_maj_min,
    msvc_find_vswhere,
    msvc_sdk_versions,
    msvc_toolset_versions,
    msvc_query_version_toolset,
)

from SCons.Tool.MSCommon.vs import (
    get_default_version,
    get_vs_by_version,
    merge_default_version,
    msvs_exists,
    query_versions,
)

from .MSVC.Policy import msvc_set_notfound_policy  # noqa: F401
from .MSVC.Policy import msvc_get_notfound_policy  # noqa: F401
from .MSVC.Policy import msvc_set_scripterror_policy  # noqa: F401
from .MSVC.Policy import msvc_get_scripterror_policy  # noqa: F401

from .MSVC.Exceptions import VisualCException  # noqa: F401
from .MSVC.Exceptions import MSVCInternalError  # noqa: F401
from .MSVC.Exceptions import MSVCUserError  # noqa: F401
from .MSVC.Exceptions import MSVCScriptExecutionError  # noqa: F401
from .MSVC.Exceptions import MSVCVersionNotFound  # noqa: F401
from .MSVC.Exceptions import MSVCSDKVersionNotFound  # noqa: F401
from .MSVC.Exceptions import MSVCToolsetVersionNotFound  # noqa: F401
from .MSVC.Exceptions import MSVCSpectreLibsNotFound  # noqa: F401
from .MSVC.Exceptions import MSVCArgumentError  # noqa: F401

from .vc import MSVCUnsupportedHostArch  # noqa: F401
from .vc import MSVCUnsupportedTargetArch  # noqa: F401
from .vc import MSVCScriptNotFound  # noqa: F401
from .vc import MSVCUseSettingsError  # noqa: F401

from .MSVC.Util import msvc_version_components  # noqa: F401
from .MSVC.Util import msvc_extended_version_components  # noqa: F401

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
