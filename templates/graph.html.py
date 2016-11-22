<html>
	<head>
		<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
		<script>
			$(function() {{
			var ctx = $("#myChart");
			
			var myChart = new Chart(ctx, {{
			    type: 'line',
			    data: {{
				datasets: [{{
				    label: 'Metric',
				    fill: false,
				    borderColor: 'rgba(0,50,255,1)',
				    data: [{data}]
				}}]
			    }},
			    options: {{
				scales: {{
				    xAxes: [{{
					type: 'linear',
					position: 'bottom'
				    }}]
				}}
			    }}
			}})}});

		</script>	
	</head>
	
	<body>
		<div style="width: 650px; margin: 0 auto;">
			<canvas id="myChart"></canvas>
			<p><b>Query:</b> {query}</p>
			<p><b>Total records found:</b> {total}</p>
			<p><b>Metric used:</b> For each record, score=6+citations</p>
		</div>
	</body>
</html>
