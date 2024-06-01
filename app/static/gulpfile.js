// gulpfile config
const {src, dest, watch, parallel} = require("gulp");

// css package
const sass = require("gulp-sass")(require('sass'));
const plumber = require("gulp-plumber");

// img package
const webp = require("gulp-webp");
const avif = require("gulp-avif")

function css(done){
    src("src/scss/**/*.scss")
        .pipe(plumber())
        .pipe(sass())
        .pipe(dest("build/css"));

    done(); // end task
}



function imageWP(done){
    const options = {
        quality: 50
    };
    src('src/img/**/**.{png,jpg}')
    .pipe(webp(options))
    .pipe(dest("build/img"));

    done(); // end task
}

function imageAV(done){
    const options = {
        quality: 50
    };
    src('src/img/**/**.{png,jpg}')
    .pipe(avif(options))
    .pipe(dest("build/img"));

    done(); // end task
}

function dev(done){
    watch("src/scss/**/*.scss", css);   
    done(); // end task
}

exports.css = css;
exports.imageWP = imageWP;
exports.imageAV = imageAV;
exports.dev = parallel(imageWP, imageAV, dev, css);