
$(function() {
	
	$('#clear').click(function() {
		$('input[type="text"]').val('');
	});
	
	$('form').submit(function(e) {
		e.preventDefault();
		
		var response = {
			"py/object": "transscrapper.structure.Response",
			"mpg": 16,
			"fuel_cost": 1756,
			"transit_time": 60,
			"landmarks": ["DMA", "Nasher"],
			"start_address": "2900 West Plano Parkway Plano, Texas 75075",
			"drive_time": 50,
			"destination_address": "2900 West Plano Parkway Plano, Texas 75075",
			"parking_price": 5,
			"drive_co2": 5,
			"transit_price": 400,
			"weather_condition": "101 F, 20% chance of rain"
		};
		
		$('#mpg').html(response.mpg);
		$('#fuel-cost').html(response.fuel_cost);
		$('#transit-time').html(response.transit_time);
		$('#landmarks').html(response.landmarks[0]);
		$('#saddr').html(response.start_address);
		$('#drive-time').html(response.drive_time);
		$('#daddr').html(response.destination_address);
		$('#parking-price').html(response.parking_price);
		$('#drive-co2').html(response.drive_co2);
		$('#transit-price').html(response.transit_price);
		$('#weather-condition').html(response.weather_condition);
	});
});
