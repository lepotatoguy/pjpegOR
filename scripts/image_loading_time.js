/*
Created on 2021

Author: @lepotatoguy

This script measures the time taken to fully load a web page and displays the result dynamically.
It:
- Records the timestamp at the start of page loading.
- Records the timestamp once the page has fully loaded (window.onload).
- Calculates the total load time in seconds.
- Updates an HTML element with id="loadtime" to display the load time in red font at size 25px.

The script assumes:
- An HTML element with id="loadtime" exists in the page.
- JavaScript execution is enabled in the browser.
- Minor typo in displayed text ("Pgae" instead of "Page")—may be intentional or requires correction.
*/

<script type="text/javascript">  
        var before_loadtime = new Date().getTime();  
        window.onload = Pageloadtime;  
        function Pageloadtime() {  
            var after_loadtime = new Date().getTime();  
            // Time calculating in seconds  
            pgloadtime = (after_loadtime - before_loadtime) / 1000  
     
            document.getElementById("loadtime").innerHTML = "Page load time is <font color='red' size= '25'><b>" + pgloadtime + "</b></font> Seconds";  
        }  
    </script>
