var gulp = require('gulp');
var sass = require('gulp-sass');
var cssmin = require('gulp-cssmin');
var browserSync = require('browser-sync').create();
var moduleImporter = require('sass-modules-importer');
var minifyjs = require('gulp-js-minify');


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

gulp.task('minify-js', function(){
  gulp.src('static/js/scripts.js')
    .pipe(minifyjs())
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

gulp.task('scripts', function(){
  gulp.watch('./static/**/*.js', ['minify-js']); 
  // Other watchers
})