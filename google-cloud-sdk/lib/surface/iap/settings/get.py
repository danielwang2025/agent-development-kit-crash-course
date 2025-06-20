# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Get IAP settings."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iap import util as iap_util

EXAMPLES = """\
          To get the IAP setting for the resources within an organization, run:

            $ {command} --organization=ORGANIZATION_ID

          To get the IAP setting for the resources within a folder, run:

            $ {command} --folder=FOLDER_ID

          To get the IAP setting for the resources within a project, run:

            $ {command} --project=PROJECT_ID

          To get the IAP setting for web type resources within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=iap_web

          To get the IAP setting for all app engine services within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=app-engine

          To get the IAP setting for an app engine service within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID

          To get the IAP setting for an app engine service version within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID
                --version=VERSION_ID

          To get the IAP setting for all backend services within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=backend-services

          To get the IAP setting for a backend service within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID

          To get the IAP setting for a regional backend service within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID
              --region=REGION_ID

          To get the IAP setting for all forwarding rules within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=forwarding-rule

          To get the IAP setting for a forwarding rule within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID

          To get the IAP setting for a regional forwarding rule within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID
              --region=REGION_ID

          """

NON_GA_EXAMPLES = EXAMPLES + """\

          To get the IAP setting for all Cloud Run services within a region of a project, run:

            $ {command} --project=PROJECT_ID --resource-type=cloud-run --region=REGION_ID

          To get the IAP setting for a Cloud Run service within a project, run:

            $ {command} --project=PROJECT_ID --resource-type=cloud-run --region=REGION_ID --service=SERVICE_ID

          """


@base.ReleaseTracks(base.ReleaseTrack.GA)
@base.DefaultUniverseOnly
class Get(base.Command):
  """Get the setting for an IAP resource."""

  detailed_help = {
      'EXAMPLES': EXAMPLES,
  }

  _support_cloud_run = False

  @classmethod
  def Args(cls, parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
        to capture some information, but behaves like an ArgumentParser.
    """
    iap_util.AddIapSettingArg(
        parser, support_cloud_run=cls._support_cloud_run,
    )
    base.URI_FLAG.RemoveFromParser(parser)

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      The IAP setting for the IAP resource.
    """
    iap_setting_ref = iap_util.ParseIapSettingsResource(
        self.ReleaseTrack(),
        args,
        self._support_cloud_run,
    )
    return iap_setting_ref.GetIapSetting()


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class GetBeta(Get):
  """Get the setting for an IAP resource."""
  detailed_help = {
      'EXAMPLES': NON_GA_EXAMPLES,
  }

  _support_cloud_run = True
