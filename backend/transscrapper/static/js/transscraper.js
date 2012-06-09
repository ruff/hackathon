
$(function() {
	
	$('#clear').click(function() {
		$('input[type="text"]').val('');
	});
	
	$('form').submit(function(e) {
		e.preventDefault();
		
		var request = {
			'car_model': $('#carmodel').val(),
			'start_address': $('#saddr').val(),
			'car_make': $('#carmake').val(),
			'destination_address': $('#daddr').val(),
			'number_people': $('#numpeople').val()
		};
		
		$.get(
			'/api',
			request,
			function(response) {
				renderResponse(response);
			},
			'json'
		);
		
		function renderResponse(response) {
			$('#mpg').html(response.mpg);
			$('#fuel-cost').html(response.fuel_cost);
			$('#transit-time').html(response.transit_time);
			$('#landmarks').html(response.landmarks[0]);
			$('#source-address').html(response.start_address);
			$('#drive-time').html(response.drive_time);
			$('#destination-address').html(response.destination_address);
			$('#parking-price').html(response.parking_price);
			$('#drive-co2').html(response.drive_co2);
			$('#transit-price').html(response.transit_price);
			$('#weather-condition').html(response.weather_condition);
		}
	});
});
