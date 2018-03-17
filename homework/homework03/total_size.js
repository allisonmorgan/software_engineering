var fs = require('fs');
// var sleep = require('sleep');
var filepath = process.argv[2];

if (!filepath) {
  return console.error('Error: No filename specified.');
}

function addFilePath(filepath) {
  return function(filename) {
    return filepath + "/" + filename;
  };
}

var all_done = function(size) {
  console.log("Total size:", size);
}

var handleFile = function(stats, i, filenames, total) {
  processFile(i+1, filenames, total+stats.size);
}

var handleDir = function(i, filenames, total) {
  fs.readdir(filenames[i], function(err, subfilenames) {
    if (err) {
      return console.error('Error: Filepath does not exist - (%s, %s)', filenames[i], err);
    }

    if (subfilenames.length == 0) { 
      // if there are no files in this directory, then continue to the next entry
      processFile(i+1, filenames, total);
    } else {
      // if there are files, get their absolute paths and add them to our list
  	  var subpath = addFilePath(filenames[i]);
      let subfilepaths = subfilenames.map(filename => { return subpath(filename)});
      var subfilenames = filenames.concat(subfilepaths)

      // pass along this bigger list, and proceed to the next entry
      // sleep.sleep(1);
      processFile(i+1, subfilenames, total);
    }
  });
}

var processFile = function(i, filenames, total) {
  // while there are still entries to loop through
  if (i < filenames.length) {
    var name = filenames[i];
    // console.log(name, Date.now());
    fs.exists(name, 
      function(exists) {
        if (exists == false) {
          return console.error('Error: File does not exist - %s', name)
        };

        fs.stat(name, function(err, stats) {
          if (err) {
            return console.error('Error: %s', err);
          }

          if (stats.isFile()) {
            handleFile(stats, i, filenames, total);
          } else if (stats.isDirectory()) {
            handleDir(i, filenames, total);
          };
        });
      });
  } else { 
    // if we've found the last entry, then return the total size
    all_done(total)
  }
}

fs.readdir(filepath, function(err, filenames) {
  if (err) {
    return console.error('Error: Filepath does not exist - (%s, %s)', filepath, err);
  }

  // filenames is the list of files and folders in the directory provided
  var path = addFilePath(filepath);
  let filepaths = filenames.map(filename => { return path(filename)})

  processFile(0, filepaths, 0);
});