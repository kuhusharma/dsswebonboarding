// Exercise 1: Create a function that adds 7 to a given number "n"
TODO: "Delete this line and fill in your code."
// ------------------


// Here's how you can use JS to modify the "DOM", which is just a term for what you see rendered when you open a website up. This is different than the .html file, and is actually the html you see when you "inspect element," which can be affected by the javascript file. 

const body = document.querySelector('body'); // now the "body" variable refers to the <body> tag in the html file
let currP = document.createElement('p'); // we are creating a <p> tag; note how this hasn't been added to the actual html file yet

currP.innerText = "Live, Love, DSS"; // this sets the text content of the <p> tag
body.appendChild(currP); // this step adds the <p> tag and its contents that we created earlier, to the webdev.html file. Note it actually modifies the DOM and not the html file itself, but don't worry about that.
// ------------------


// Exercise 2: Create 10 <p> tags, with their contents being the first 10 multiples of 7, starting from 7.
TODO: "Delete this and fill in your code."


// If you would like to learn more about how JS can be used to modify the page being shown on your browser (the "DOM"), check out this resource: https://www.theodinproject.com/lessons/foundations-dom-manipulation-and-events
