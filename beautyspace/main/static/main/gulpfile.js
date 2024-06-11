'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const sourcemaps = require('gulp-sourcemaps');
const browserSync = require('browser-sync').create();

function buildStyles() {
    return gulp.src('./style.scss')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest('./stylesheet'))
        .pipe(browserSync.stream());
};

function watchFiles() {
    browserSync.init({
        proxy: "localhost:8000", // Ваш локальный сервер
        port: 3000
    });

    gulp.watch('./style.scss', buildStyles);
    gulp.watch("./**/*.html").on('change', browserSync.reload);
}

gulp.task('default', watchFiles);
