import sqlite3

con = sqlite3.connect('db/gambling_cat.db', check_same_thread=True)

cur = con.cursor()

######################################################################
#                                                                    #
#  Uncomment below section and change VALUES section appropriatelly  #
#  for the first bot start up.                                       #
#  Then - shutdown bot & comment these line out again.               #
#                                                                    #
######################################################################
#
#cur.execute("""CREATE TABLE users(
#     userid text,
#     username text,
#     address text,
#     balance real
#     )""")
#cur.execute("INSERT INTO users VALUES ('BotID-goes-here', 'BotName#XXX-goes-here', 'Bot-Assigned-Wallet-Address-goes-here', '0')")
#
#####################################################################
#cur.execute("SELECT * FROM users")

def createWallet(raw, username, address, balance):
    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
              (str(raw), str(username), str(address['result']), str(balance['result'])))
    con.commit()


cur.execute("SELECT * FROM users")
print(cur.fetchall())

con.commit()
#con.close()
