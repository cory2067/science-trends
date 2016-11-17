//Script to be injected into webpage to extract data

record = 1;
ready = 1;

$(function() {
setInterval(function() {
        if(ready == 1) {
                $("#select2-chosen-1").mouseup()
                $("#numberOfRecordsRange").click();
                $("#markFrom").val(record)
                $("#markTo").val(record + 499)
                $('#bib_fields option:eq(2)').prop('selected', true)
                $('#saveOptions option:eq(1)').prop('selected', true)
                $(".quickoutput-action")[0].click();
                record += 500;
                console.log(record);
                ready = 0;
        } else if(ready === 0 && $(".quickoutput-action > input").length > 0) {
                setTimeout(function() { ready = 1; }, 2000);
                ready = -1;
        }
}, 500)
});

