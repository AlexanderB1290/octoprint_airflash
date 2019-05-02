/*
 * View model for AirFlash Uploader
 *
 * Author: Aleksandar B
 * License: GPLv3
 */
$(function() {
    function AirflashViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];
        self.loginState = parameters[1];
        self.printerState = parameters[2];
        self.filesViewModel = parameters[3];

        self.uploadButton = undefined;
        self.uploadProgress = undefined;
        self.uploadProgressBar = undefined;

        self.uploadProgressText = ko.observable();
        self.isPrinting = ko.observable(undefined);

        self.onStartup = function(){
            self.uploadButton = $("#gcodeUploadAF");
            self.uploadProgress = $("#uploadProgressAF");
            self.uploadProgressBar = $(".bar", self.uploadProgress);
        };

        self.onAfterBinding = function(){
            self.filesViewModel.uploadButton = self.uploadButton;
            self.filesViewModel.uploadProgress = self.uploadProgress;
            self.filesViewModel.uploadProgressBar = self.uploadProgressBar;
        };

    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: AirflashViewModel,
        dependencies: ["settingsViewModel", "loginStateViewModel", "printerStateViewModel", "filesViewModel"],
        elements: ["#sidebar_plugin_airflash"]
    });
});
