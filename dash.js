var dash_button = require('node-dash-button')
var exec = require('child_process').exec, child;;
var dash = dash_button("50:f5:da:af:12:e8", null, null, 'all'); //address from step above
dash.on("detected", function (){
    console.log("omg found");

	child = exec('python3 toggle.py username password bool,
		function (error, stdout, stderr) {
			console.log('stdout: ' + stdout);
			console.log('stderr: ' + stderr);
			if (error !== null) {
				 console.log('exec error: ' + error);
			}
		});
});

console.log('APP IS NOW RUNNING');
