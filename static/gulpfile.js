const gulp = require("gulp");
const watch = require("gulp-watch");
const sourcemaps = require("gulp-sourcemaps");
const sass = require("gulp-sass");
const postcss = require("gulp-postcss");
const autoprefixer = require("autoprefixer");

const webpack = require("webpack");
const webpackStream = require("webpack-stream");

/**
 * ====================
 * === SASS compile ===
 * ====================
 */
gulp.task("styles", function() {
    return gulp.src("./src/styles/index.scss")
        .pipe(sourcemaps.init())
        .pipe(
            sass({
                outputStyle: "compressed",
                includePaths: ["./node_modules/"]
            })
                .on("error", sass.logError)
        )
        .pipe(
            postcss([
                autoprefixer(),
            ])
        )
        .pipe(sourcemaps.write())
        .pipe(gulp.dest("./dist"));
});
/* == SASS watch == */
gulp.task("styles:watch", function() {
    gulp.watch("./src/styles/**/*.scss", gulp.series("styles"));
});

/**
 * ==========================
 * === TypeScript compile ===
 * ==========================
 */
gulp.task("scripts", function() {
    // ./src/scripts/index.ts
    return gulp.src("./src/scripts/index.ts")
        .pipe(webpackStream({
            devtool: "inline-source-map",
            mode: "development",
            module: {
                rules: [
                    {
                        test: /\.tsx?$/,
                        use: "ts-loader",
                        exclude: /node_modules/
                    }
                ]
            },
            resolve: {
                extensions: [".tsx", ".ts", ".js"]
            },
            output: {
                filename: "index.js",
            }
        }))
        .pipe(gulp.dest("./dist/"))
});
/* == TypeScript watch == */
gulp.task("scripts:watch", function() {
    gulp.watch("./src/scripts/**/*.ts", gulp.series("scripts"));
});

/**
 * ==================
 * === Build Task ===
 * ==================
 */
gulp.task("build", gulp.parallel("styles", "scripts"))

/**
 * ====================
 * === Default Task ===
 * ====================
 */
gulp.task("default", gulp.series("styles", "scripts", gulp.parallel("styles:watch", "scripts:watch")));
