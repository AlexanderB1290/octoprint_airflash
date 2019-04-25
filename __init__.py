# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class AirFlashPlugin(octoprint.plugin.StartupPlugin,
					 octoprint.plugin.AssetPlugin,
					 octoprint.plugin.TemplatePlugin,
					 octoprint.plugin.SettingsPlugin):
	def on_after_startup(self):
		print "AirFlash initialized"

	def get_template_configs(self):
		return [
			dict(type="sidebar", template="airflash_sidebar.jinja2"),
			dict(type="settings", template="airflash_settings.jinja2")
		]

	def get_settings_defaults(self):
		return dict(
			ip_address="flashair",
			upload_path="/upload.cgi",
			auth=dict(
				enabled=False,
				type="Basic",
				username="admin",
				password="1234"
			)
		)

	def on_settings_save(self, data):
		old_ip = self._settings.get_string(["ip_address"])
		old_up_path = self._settings.get_string(["upload_path"])

		old_auth_enabled = self._settings.get_boolean(["auth", "enabled"])
		old_auth_type = self._settings.get_string(["auth", "type"])
		old_auth_user = self._settings.get_string(["auth", "username"])
		old_auth_pwd = self._settings.get_string(["auth", "password"])

		new_settings = octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

		new_ip = self._settings.get_string(["ip_address"])
		if old_ip != new_ip:
			self._logger.info("changed AirFlash IP address from '{old_ip}' to '{new_ip}'").format(**locals())

		new_up_path = self._settings.get_string(["upload_path"])
		if old_up_path != new_up_path:
			self._logger.info("changed AirFlash upload path from '{old_up_path}' to '{new_up_path}'").format(**locals())

		new_auth_enabled = self._settings.get_boolean(["auth", "enabled"])
		if old_auth_enabled != new_auth_enabled:
			self._logger.info(
				"changed AirFlash authentication from '{old_auth_enabled}' to '{new_auth_enabled}'").format(**locals())
			if new_auth_enabled == True:
				new_auth_type = self._settings.get_string(["auth", "type"])
				if old_auth_type != new_auth_type:
					self._logger.info(
						"changed AirFlash authentication type from '{old_auth_type}' to '{new_auth_type}'").format(
						**locals())

				new_auth_user = self._settings.get_string(["auth", "username"])
				new_auth_pwd = self._settings.get_string(["auth", "password"])
				if old_auth_user != new_auth_user or old_auth_pwd != new_auth_pwd:
					self._logger.info("updated AirFlash authentication credentials ")
		return new_settings

__plugin_name__ = "AirFlash Uploader"
__plugin_description__ = "Uploading files to AirFlash Wi-Fi SD card"
__plugin_url__ = ""
__plugin_author__ = "Aleksandar Bushev"

__plugin_implementation__ = AirFlashPlugin()
