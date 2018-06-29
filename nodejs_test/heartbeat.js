var spawn = require('child_process').spawn;
	py = spawn('python', ['heartbeat.py']);
	string = ''; 

py.stdout.on('data', function(data){
	string += data;
});	

py.stdout.on('end', function(){
	console.log(string);
});

py.stdin.write(JSON.stringify("hello!"));
py.stdin.write(JSON.stringify("world!"));
py.stdin.write(JSON.stringify("/close"));
py.stdin.end();