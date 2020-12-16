$(document).ready(function() {

	$("#error_alert").hide();

	$('form').on('submit', function(event) {

		event.preventDefault();

		var formData = new FormData($('form')[0]);

		$.ajax({
			/*
			xhr : function() {
				var xhr = new window.XMLHttpRequest();

				xhr.upload.addEventListener('progress', function(e) {

					if (e.lengthComputable) {

						console.log('Bytes Loaded: ' + e.loaded);
						console.log('Total Size: ' + e.total);
						console.log('Percentage Uploaded: ' + (e.loaded / e.total))

						var percent = Math.round((e.loaded / e.total) * 100);
						$('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
					}

				});

				return xhr;
			},*/
			type : 'POST',
			url : '/',
			data : formData,
			processData : false,
			contentType : false,
			success : on_recieve_prediction
		});

	});

});

function on_recieve_prediction(data)
{   
    if(data.error) {
        $("#error_alert").text(data.error).show();
        $("#prediction_container").html("");
    }
    else {
        $("#error_alert").hide();
        $("#prediction_container").html(data.prediction_display_html);
    }   
}