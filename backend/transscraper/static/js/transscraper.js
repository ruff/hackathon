
$(function() {

	var testMode = false;
	
	$('#results').hide();
	
	$('#clear').click(function(e) {
		e.preventDefault();
		$('input[type="text"]').val('');
		$('#results').fadeOut('fast');
	});
	
	$('#searchform').submit(function(e) {
		e.preventDefault();
		
		if (testMode) {
			var response = {
				'mpg': 16,
				'fuel_cost': 17.56,
				'transit_time': 60.3333,
				'landmarks': ['DMA', 'Nasher'],
				'start_address': '2900 West Plano Parkway Plano, Texas 75075',
				'drive_time': 50,
				'destination_address': '2900 West Plano Parkway Plano, Texas 75075',
				'parking_price': 5,
				'drive_co2': 5,
				'transit_price': 4.00,
				'weather_condition': '101 F, 20% chance of rain',
				'savings': 30
			};
			
			renderResponse(response);
		}
		else {
			$.get(
				'/api',
				{
					'car_model': $('#carmodel').val(),
					'start_address': $('#saddr').val(),
					'car_make': $('#carmake').val(),
					'destination_address': $('#daddr').val(),
					'number_people': $('#numpeople').val()
				},
				function(response) {
					renderResponse(response);
				},
				'json'
			);
		}
		
		function renderResponse(response) {
			$('#mpg').html(response.mpg + ' MPG');
			$('#fuel-cost').html('$' + response.fuel_cost.toFixed(2));
			$('#transit-time').html(response.transit_time.toFixed(0) + ' minutes');
			$('#landmarks').html(response.landmarks[0]);
			$('#source-address').html(response.start_address);
			$('#drive-time').html(response.drive_time.toFixed(0) + ' minutes');
			$('#destination-address').html(response.destination_address);
			$('#parking-price').html('$' + response.parking_price.toFixed(2));
			$('#drive-co2').html(response.drive_co2 + ' lbs');
			$('#transit-price').html('$' + response.transit_price.toFixed(2));
			$('#weather-condition').html(response.weather_condition);
			
			if (response.savings > 0) {
				$('#savings').html('$' + response.savings.toFixed(2));
			}
			else {
				$('#savings').html('-$' + (-response.savings.toFixed(2)));
			}
			
			$('#results').fadeIn('fast');
			
			$('#donate').hide();
			
			if (response.savings > 0) {
				$('#donate').fadeIn('slow');
			}
			
			scrollBottom();
		}
		
		function scrollBottom() {
			$('html, body').animate({ scrollTop: $("#results").offset().top }, 500);
		}
	});
});
