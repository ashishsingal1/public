import uuid

def DataTable(df):
    """ Prints a pandas.DataFrame as JQuery DataTables """
    from IPython.display import HTML
    # Generate random container name
    id_container = uuid.uuid1()
    output = """
        <div id="datatable-container-%s">
            <link rel="stylesheet" type="text/css" href="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.0/css/jquery.dataTables.css">
            <link rel="stylesheet" type="text/css" href="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.0/css/jquery.dataTables_themeroller.css">
            <script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.0/jquery.dataTables.min.js"></script>

            <script type="text/javascript">
                var url = window.location.href;

                if(url.indexOf("localhost:9999") != -1){
                    $('#datatable-container-%s table.datatable').dataTable();
                } else {
                    $.getScript("http://code.jquery.com/jquery-1.11.1.min.js");
                    $(document).ready(function() {
                        $('#datatable-container-%s table.datatable').dataTable();
                    });
                }

            </script>
            <!-- Insert table below -->
            %s
        </div>
    """ % (id_container, id_container, id_container, df.to_html(index=False, classes="datatable dataframe"))
    return HTML(output)