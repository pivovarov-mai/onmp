using OnmpApp.Models.Database;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OnmpApp.Converters;

public class CatalogStatusToStringConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value is CatalogType catalogType)
        {
            return catalogType switch
            {
                CatalogType.Diagnose => Properties.Resources.Diagnose,
                CatalogType.Medicine => Properties.Resources.Medicine,
                CatalogType.Disease => Properties.Resources.Disease,
                _ => Properties.Resources.UnknownType,
            };
        }

        return Properties.Resources.UnknownType;
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
