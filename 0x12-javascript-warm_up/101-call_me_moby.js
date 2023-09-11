#!/usr/bin/node

function callMeMoby(X, theFunction) {
	for (let i = 0; i < X; i++) {
		theFunction();
	}
}

module.exports = {
	callMeMoby: callMeMoby
};
