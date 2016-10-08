var dash_button = require('node-dash-button');
var dash = dash_button("50:f5:da:af:12:e8", null, null, 'all'); //address from step above
dash.on("detected", function (){
    console.log("omg found");
});

console.log('APP IS NOW RUNNING');
