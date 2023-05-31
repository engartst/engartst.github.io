function setup() {
  createCanvas(800, 800);
}

function draw() {
	background(110);
	noStroke();
	fill(199, 23);
	ellipse(width/2 + mouseX, height/2 + mouseY, 100, 100);
	rectMode(RADIUS);
	fill(222, 33);
	rect(width/2 - mouseX, height/2 - mouseY, 20, 20, 2, 3, 4, 5);
	fill(255, 12);
	triangle(width/2 + mouseX, height/2 - mouseY, 200 + mouseX, 200 - mouseY, 100 + mouseX, 100 - mouseY);
	fill(12, 222);
	
}
