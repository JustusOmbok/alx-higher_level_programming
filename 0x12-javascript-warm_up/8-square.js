#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length !== 1 || isNaN(parseInt(args[0]))) {
	console.log("Missing size");
} else {
	const size = parseInt(args[0]);

	if (size > 0) {
		for (let i = 0; i < size; i++) {
			let row = '';
			for (let j = 0; j < size; j++) {
				row += 'X';
			}
			console.log(row);
		}
	}
}
