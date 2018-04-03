var gulp = require('gulp');
var sass = require('gulp-sass');
var cssmin = require('gulp-cssmin');
var browserSync = require('browser-sync').create();
var moduleImporter = require('sass-modules-importer');

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