using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OnmpApp.Models.Database;
using OnmpApp.Properties;

namespace OnmpApp.Database;

public static class CardTable
{
    public static async Task<List<Card>> Search(string searchText, bool draftChecked, bool readyChecked,
        bool templateChecked, bool archiveChecked, int skip, int take)
    {
        searchText = searchText.ToLower();

        if(skip == -1 || take == -1)
            return await BaseDatabase.DB.Table<Card>().Where(el => el.UserId == Settings.UserId && el.LowerName.Contains(searchText)
                           && ((draftChecked && el.Status == CardStatus.Draft) ||
                              (readyChecked && el.Status == CardStatus.Ready) ||
                              (templateChecked && el.Status == CardStatus.Template) ||
                              (archiveChecked && el.Status == CardStatus.Archive))).OrderByDescending(el => el.Id).ToListAsync();



        var res = await BaseDatabase.DB.Table<Card>().Where(el => el.UserId == Settings.UserId && el.LowerName.Contains(searchText)
                           && ((draftChecked && el.Status == CardStatus.Draft) ||
                              (readyChecked && el.Status == CardStatus.Ready) ||
                              (templateChecked && el.Status == CardStatus.Template) ||
                              (archiveChecked && el.Status == CardStatus.Archive))).OrderByDescending(el => el.Id).Skip(skip).Take(take).ToListAsync();

        return res;
    }

    public static async Task<bool> Insert(Card card)
    {
        card.LowerName = card.Name.ToLower();
        _ = await BaseDatabase.DB.InsertAsync(card);
        return true;
    }
    public static async Task<bool> Update(Card card)
    {
        card.LowerName = card.Name.ToLower();
        _ = await BaseDatabase.DB.UpdateAsync(card);
        return true;
    }

    public static async Task<bool> Remove(int id)
    {
        _ = await BaseDatabase.DB.DeleteAsync<Card>(id);
        return true;
    }

    public static async Task<Card> Get(int id)
    {
        return await BaseDatabase.DB.GetAsync<Card>(id);
    }

    public static async Task<string> GetLastOrder()
    {
        var card = await BaseDatabase.DB.Table<Card>().Where(el => el.UserId == Settings.UserId).OrderByDescending(el => el.Id).FirstOrDefaultAsync();
        return card == null ? "" : card.Order;
    }
}
