class Dates {
    static formatToYMD(date, div = true) {
        var day  = date.split("/")[0];
        var month  = date.split("/")[1];
        var year  = date.split("/")[2];
        
        if (div) return new Date(year + '-' + ("0" + month).slice(-2) + '-' + ("0" + day).slice(-2));
        return new Date(year + ("0" + month).slice(-2) + ("0" + day).slice(-2));
    }

    static formatToDMY(date, div = true) {
        var year  = date.split("-")[0];
        var month  = date.split("-")[1];
        var day  = date.split("-")[2];
        
        if (div) return ("0" + day).slice(-2) + '/' + ("0" + month).slice(-2) + '/' + year;
        return year  + ("0" + month).slice(-2) + ("0" + day).slice(-2);
    }
}

module.exports = Dates;