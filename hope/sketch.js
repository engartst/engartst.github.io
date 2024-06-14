var x;
var y;
var speed = 5;
var dx;
var dy;
var which = 0;
var bounce = 0;

function setup() {
    createCanvas(windowWidth, windowHeight);
    x = random(width);
    y = random(height);
    dx = random(3);
    dy = random(3);
    background(0);
}

function windowResized() {
   resizeCanvas(windowWidth, windowHeight);
}

function draw() {
    background(0);
    textSize(64);
    textAlign(CENTER);
    textFont("League Gothic")
    if (bounce % 2 == 0) {
        fill(255);
        text('HOPE', width / 2, height / 2);
    }
    if (bounce % 2 == 1) {
        fill(255, 0, 0);
        text('HOP913', width / 2, height / 2);
    }
    fill(255);
    letter = ["H", "0", "P", "9", "1", "3"];

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
    x = x + (dx * speed);
    y = y + (dy * speed);

}
