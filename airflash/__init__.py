# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class AirflashPlugin(octoprint.plugin.StartupPlugin,
					 octoprint.plugin.TemplatePlugin,
					 octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin):

	##~~ StartupPlugin mixin

	def on_after_startup(self):
		self._logger.info("AirFlash initialized")

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			ip_address='flashair',
			upload_path='/upload.cgi',
			auth=dict(
				enabled=False,
				type='basic',
				user='admin',
				pwd='1234'
			)
		)

	def on_settings_save(self, data):
		# For debug purpose only
		self._logger.info("New data: {data}".format(**locals()))
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

	##~~ TemplatePlugin and AssetPlugin mixin

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/airflash.js"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			airflash=dict(
				displayName="Airflash Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="AlexanderB1290",
				repo="octoprint_airflash",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/AlexanderB1290/octoprint_airflash/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "AirFlash Uploader"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AirflashPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

