import '../css/main.less'
import build_header from './construction/header.js'
import build_footer from './construction/footer.js'



let teststring = "here we go"

console.log(teststring)

function component() {
	let element = document.createElement('div')

	element.classList.add('masketta_clan')

	return element
}

document.body.appendChild(component());



