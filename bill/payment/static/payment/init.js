(function($){
  $(function(){
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
    });
    $(document).ready(function(){
    $('.collapsible').collapsible();
    });
    $(document).ready(function(){
    $('.tooltipped').tooltip({delay: 50});
    });

    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250',
        "Mohit Udupa" : null,
        "Manthan Suresh" : null,
        "Hemant Khaitan" : null,
        "Stroman Kenya" : null,
        "Crist Trace" : null,
        "Hane Burnice" : null,
        "Jacobi Emory" : null,
        "Wunsch Rozella" : null,
        "Yundt Amie" : null,
        "Boehm Elmira" : null,
        "Haley Laurine" : null,
        "Wiegand Carley" : null,
        "Jacobi Jamil" : null,
        "Strosin Rodrigo" : null,
        "VonRueden Cleveland" : null,
        "Towne Katelyn" : null,
        "Mann Tracy" : null,
        "Renner Donnie" : null,
        "Dickens Brody" : null,
        "Crooks Eduardo" : null,
        "Gulgowski Evans" : null,
        "Gislason Dusty" : null,
        "D'Amore Pattie" : null,
        "Blanda Sanford" : null,
        "Schowalter Jackeline" : null,
        "Kautzer Eula" : null,
        "Ortiz Celestino" : null,
        "Kub Michale" : null,
        "VonRueden Dario" : null,
        "Jacobs Helene" : null,
        "manasvin m" : null
    },
    });
  }); // end of document ready
})(jQuery); // end of jQuery name space
