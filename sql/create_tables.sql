CREATE TABLE IF NOT EXISTS google_accounts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user VARCHAR(254) NOT NULL,
  date DATE,
  listing_on_search INT,
  listing_on_maps INT,
  visit_your_website INT,
  request_directions INT,
  call_you INT,
  chat_to_you INT,
  UNIQUE KEY google_accounts_key(user, date)
);
