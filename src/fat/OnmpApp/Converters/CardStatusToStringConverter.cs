using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using OnmpApp.Models;
using OnmpApp.Models.Database;

namespace OnmpApp.Converters;

// Конвертер для преобразования типа карты в текстовое поле
public class CardStatusToStringConverter : IValueConverter
{
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value is CardStatus cardStatus)
        {
            return cardStatus switch
            {
                CardStatus.Draft => Properties.Resources.Draft,
                CardStatus.Ready => Properties.Resources.Ready,
                CardStatus.Template => Properties.Resources.Template,
                CardStatus.Archive => Properties.Resources.Archive,
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