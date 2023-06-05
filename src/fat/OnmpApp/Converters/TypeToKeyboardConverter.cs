using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Converters;

public class TypeToKeyboardConverter : IValueConverter
{
    public object Convert(object value, Type targetType = null, object parameter = null, CultureInfo culture = null)
    {
        if (value is Type type)
        {
            if (type == typeof(int) || type == typeof(double) || type == typeof(float) || type == typeof(decimal))
            {
                return Keyboard.Numeric;
            }
        }

        return Keyboard.Default;
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
