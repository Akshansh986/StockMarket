class Util:
    def flatten(self, date_price_list):
        print("Flattening data")
        result = []
        for date_price in date_price_list:
            for time_price in date_price.get_time_price_list():
                result.append(time_price.get_price())

        filtered_result = [x for x in result if x is not None]
        print("Total data ponits : " + str(len(result)))
        print("Final data points after null filter : " + str(len(filtered_result)))
        return filtered_result