var spawn = require('child_process').spawn,
	py = spawn('python', ['sum.py']),
	data = [1,2,3,4,5]
	string = '';


py.stdout.on('data', function(data){
	string += data.toString();
});

py.stdout.on('end', function(){
	console.log(string); 
})

py.stdin.write(JSON.stringify(data));
py.stdin.end();