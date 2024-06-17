// vars to be set later
var x;
var y;
var speed;
var dx;
var dy;

// vars set now
var which = 0;
var bounce = 0;

// constant
const word = "HOP913";

function setup() {
    // this loop runs once on load

    // this is how you set the seed for random
    // you can put anything you want in the parenthesis
    // this is if you want the random to be the same every time
    randomSeed(69420);

    // this makes the canvas the size of the window
    createCanvas(windowWidth, windowHeight);

    // this places the moving text randomly
    // you could also set it to a specific location
    x = random(width);
    y = random(height);

    // this sets the speed of the text randomly between -3 and 3
    // you could also set it to a specific speed
    dx = random(-3, 3);
    dy = random(-3, 3);

    // this sets the speed of the text randomly between -10 and 10
    speed = random(-25, 25);

    // draw the background so there is not a blip
    background(0);

    // load any fonts here
    textFont("League Gothic")
}

function windowResized() {
    // this is a magic p5js function that we can use
    // this deals with window resizing after the initial setup
    resizeCanvas(windowWidth, windowHeight);
}

function mousePressed() {
    // this is a magic p5js function that we can use
    if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
        // this is how you save a canvas
        saveCanvas('HOPE', 'png');
    }
}

function draw() {
    // this loop runs every frame
    // you can set frame speed if you want
    frameRate(60);

    // if you don't redraw the background you get a trail
    background(0);

    // you could do this with if statements
    if (bounce % 3 == 0) {
        fill(255, 255, 0);
    } else if (bounce % 3 == 1) {
        fill(0, 255, 255);
    } else if (bounce % 3 == 2) {
        fill(255, 0, 255);
    } else {
        fill(255, 255, 255);
    }

    // this is how you split a string into an array of characters
    letter = split(word, '');
    // we could do this but that means to change you would have
    // to dive into the code and that is annoying
    //letter = ["H", "0", "P", "9", "1", "3"];

    // this is changing the direction and picking a new letter on bounce
    if (x >= width || x <= 0) {
        dx = dx * -1;
        bounce = bounce + 1;
        if (which < letter.length - 1) {
            which = which + 1;
        } else {
            which = 0;
        }
    }
    if (y >= height || y <= 0) {
        dy = dy * -1;
        bounce = bounce + 1;
        if (which < letter.length - 1) {
            which = which + 1;
        } else {
            which = 0;
        }
    }

    // I purposely did not set a max size for the text
    // how could you prevent catastrophic failure?
    t_size = 64 + bounce * 5;
    textSize(t_size);

    // here is how you do it with a switch statement
    // what happens when you change the length of the array?
    switch (which) {
        case 0:
            text(letter[0], x, y);
            break;
        case 1:
            text(letter[1], x, y);
            break;
        case 2:
            text(letter[2], x, y);
            break;
        case 3:
            text(letter[3], x, y);
            break;
        case 4:
            text(letter[4], x, y);
            break;
        case 5:
            text(letter[5], x, y);
            break;
    }

    // this is how you move the text
    x = x + (dx * speed);
    y = y + (dy * speed);

    // starting here is the static text
    textSize(64);
    textAlign(CENTER);

    // every bounce change text and color
    if (bounce % 2 == 0) {
        fill(255);
        text('HOPE', width / 2, height / 2);
    } else if (bounce % 2 == 1) {
        fill(255, 0, 0);
        text('HOP913', width / 2, height / 2);
    } else {
        fill(255, 0, 0);
        text('HOP913', width / 2, height / 2);
    }
}
