# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class AirflashPlugin(octoprint.plugin.StartupPlugin,
					 octoprint.plugin.TemplatePlugin,
					 octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin):

	# noinspection PyMissingConstructor
	def __init__(self):
		self._ip_address = 'flashair'
		self._upload_path = '/upload.cgi'

	def initialize(self):
		self._ip_address = self._settings.get(["ip_address"])
		self._upload_path = self._settings.get(["upload_path"])

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

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def on_settings_save(self, data):
		self._logger.info("New data: {data}".format(**locals()))
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/airflash.js"],
			css=["css/airflash.css"],
			less=["less/airflash.less"]
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


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "AirFlash Uploader"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = AirflashPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

