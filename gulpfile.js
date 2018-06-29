var gulp = require('gulp');
var sass = require('gulp-sass');
var cssmin = require('gulp-cssmin');
var browserSync = require('browser-sync').create();
var moduleImporter = require('sass-modules-importer');
var minifyjs = require('gulp-js-minify');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');

gulp.task('hello', function() {
  console.log('Hello Zell');
});

gulp.task('sass', function(){
  return gulp.src('static/css/main.scss')
    .pipe(sass({ importer: moduleImporter() }))
    .pipe(cssmin())
    .pipe(gulp.dest('static/css/'))
    .pipe(browserSync.stream());
});

gulp.task('scripts', function() {
    return gulp.src('static/js/main.js')
        .pipe(concat('scripts.js'))
        .pipe(gulp.dest('static/js/'))
        .pipe(rename('scripts.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/js/'));
});

gulp.task('browserSync', function() {
  browserSync.init({
    server: {
      baseDir: 'ball-is-fun'
    },
  })
})


gulp.task('watch', function(){
  gulp.watch('./static/**/*.scss', ['sass']); 

  // Other watchers
})

gulp.task('script', function(){
  gulp.watch('./static/**/*.js', ['scripts']); 

  // Other watchers
})

// gulp.task('scripts', function(){
//   // Other watchers
// })