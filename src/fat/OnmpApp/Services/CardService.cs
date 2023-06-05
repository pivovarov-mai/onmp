using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Database;
using OnmpApp.Helpers;
using OnmpApp.Models.Database;

namespace OnmpApp.Services;

public static class CardService
{

    // Получение списка карточек
    public static async Task<List<Card>> Search(string searchText, bool draftChecked, bool readyChecked,
                                        bool templateChecked, bool archiveChecked, int skip = 0, int take = 15)
    {
        try
        {
            return await CardTable.Search(searchText, draftChecked, readyChecked, templateChecked, archiveChecked, skip, take);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }

        return null;
    }

    // Обновление карточки
    public static async Task<bool> Update(Card card)
    {
        try
        {
            return await CardTable.Update(card);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }
        return false;

    }

    public static async Task<string> GetLastOrder()
    {
        try
        {
            return await CardTable.GetLastOrder();
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }
        return "";
    }


    // Удаление карточки
    public static async Task<bool> Remove(int id)
    {
        try
        {
            await CardTable.Remove(id);
            await FullCardTable.Remove(id);
            return true;
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }

        return false;

    }


    // Получение краткой информации карточки
    public static async Task<Card> Get(int id)
    {
        try
        {
            return await CardTable.Get(id);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }

        return null;
    }

    // Добавление карточки
    public static async Task<bool> Insert(Card card)
    {
        try
        {
            return await CardTable.Insert(card);
        }
        catch (Exception ex)
        {
#if DEBUG
            Debug.WriteLine(@"\tERROR {0}", ex.Message);
#endif
            ToastHelper.Show(Properties.Resources.Error);
        }

        return false;
    }
}