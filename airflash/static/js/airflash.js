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

        self.uploadUrl = "";
        self.settings = undefined;
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
            console.dir();
            self.settings = self.settingsViewModel.settings.plugins.airflash;
            self.uploadUrl = "http://"+self.settings.ip_address()+""+self.settings.upload_path();
        };

        self.afUpload = function(data, e){
            var fileList = e.target.files;
            if(fileList.length > 0){
                var formData = new FormData();
                for(var i=0; i<fileList.length; i++){
                    var fl = fileList.item(i);
                    formData.append(fl.name, fl, fl.name);
                }
                $.ajax({
                    url: self.uploadUrl,
                    type: "POST",
                    data: formData,
                    processData: false,
                    contentType: false,
                    crossDomain: true,
                    headers:{
                        "Access-Control-Allow-Origin": "*"
                    },
                    success: function(result){
                        console.log("File uploaded");
                    },
                    error: function(error){
                        console.error(error);
                    }
                });
            }
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
