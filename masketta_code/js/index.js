import '../css/style.less'
import Bane from '../images/bane.jpg'

var teststring = "here we go"

console.log(teststring)

function component() {
	var element = document.createElement('div')

	element.classList.add('masketta_clan')
	var myBane = new Image()
	myBane.src = Bane

	element.appendChild(myBane)

	return element
}

document.body.appendChild(component());



