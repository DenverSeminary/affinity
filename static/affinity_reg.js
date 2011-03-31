$(document).ready(
				function () {
					$('#id').keyup( function () {
						$('#data_modal').css('display','block');	
					});
					$('#fetch').click( function () {
						$('#more_info').slideToggle();
						$('#data_modal').fadeOut().remove();					
					});
					$('input[type=text]').each(function() {
						var default_value = this.value;
						$(this).focus(function() {
							if(this.value == default_value) {
								this.value = '';
							}
						});
						$(this).blur(function() {
							if(this.value == '') {
								this.value = default_value;
							}
						});
					});	
				});
