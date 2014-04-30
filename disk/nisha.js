/**
 * Created by prism on 4/29/14.
 */
/** Get Folders or Files name from DVD */

var exec = require('child_process').exec,
    fs = require('fs');
/**
 * Get current user name
 */
/*function User(cb) {
    exec('whoami',function (error, stdout, stderr) {
            if(error)
            return cb(error);
        cb(null,stdout);
        });
}*/

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
            exec('whoami',function(err , stdoutt , stderr){
                process.chdir("/media/" + stdoutt + '/' + stdout + "/");
            });
            //process.chdir("/media/" + User() + '/' + stdout + "/");
            return fs.readdirSync(process.cwd());
        });
}

/*
Eject DVD drive
 */
module.exports = function Eject(){
    exec('eject',function(error , stdout,stderr){
        if(error)
        console.log(error);
    });
}

function Eject(){
    exec('eject',function(error , stdout,stderr){
        if(error)
            console.log(error);
    });
}

function Hiren() {
    exec('volname /dev/sr0',
        function (error, stdout, stderr) {
            if (stdout == ( "volname: No medium found" || "volname: Input/output error" ))
                Hiren();
            else {}
            exec('whoami',function(err , user , stderr){
                //process.chdir("/media/" + stdoutt + '/' + stdout + "/");
                console.log("/media/" + user + "/" + stdout + "/");
            });
            return fs.readdirSync(process.cwd());
        });
}

Hiren()