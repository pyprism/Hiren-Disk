/**
 * Created by prism on 4/29/14.
 */
/** Get Folders or Files name from DVD */

var exec = require('child_process').exec,
    fs = require('fs');
/**
 * Get current user name
 */
function User() {
    exec('whoami',
        function (error, stdout, stderr) {
            return stdout;
        });
}

/*
 Go to DVD and return contents names
 */
module.exports = function Hiren() {
    exec('volname /dev/sr0',
        function (error, stdout, stderr) {
            if (stdout == ( "volname: No medium found" || "volname: Input/output error" ))
                Hiren();
            else
                pass;
            process.chdir("/media/" + User() + '/' + stdout + "/");
            return fs.readdirSync(process.cwd());
        });
}

