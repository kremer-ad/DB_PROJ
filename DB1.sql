CREATE TABLE Area
(
  AreaId INT NOT NULL,
  AreaName INT NOT NULL,
  PRIMARY KEY (AreaId)
);

CREATE TABLE City
(
  CityName INT NOT NULL,
  AreaId INT NOT NULL,
  PRIMARY KEY (CityName),
  FOREIGN KEY (AreaId) REFERENCES Area(AreaId)
);

CREATE TABLE Client
(
  ClientId INT NOT NULL,
  PhoneNumber INT NOT NULL,
  Address INT NOT NULL,
  ClientName INT NOT NULL,
  CityName INT NOT NULL,
  AgentId INT NOT NULL,
  PRIMARY KEY (ClientId),
  FOREIGN KEY (CityName) REFERENCES City(CityName),
  FOREIGN KEY (AgentId) REFERENCES Agent(AgentId)
);

CREATE TABLE Agent
(
  AgentId INT NOT NULL,
  AgentName INT NOT NULL,
  Rating INT NOT NULL,
  HireYear INT NOT NULL,
  Salary INT NOT NULL,
  AreaId INT NOT NULL,
  Boss_AgentId INT NOT NULL,
  PRIMARY KEY (AgentId),
  FOREIGN KEY (AreaId) REFERENCES Area(AreaId),
  FOREIGN KEY (Boss_AgentId) REFERENCES Agent(AgentId)
);

CREATE TABLE Schedule
(
  MeetingTime INT NOT NULL,
  ClientId INT NOT NULL,
  AgentId INT NOT NULL,
  PRIMARY KEY (MeetingTime),
  FOREIGN KEY (ClientId) REFERENCES Client(ClientId),
  FOREIGN KEY (AgentId) REFERENCES Agent(AgentId),
  UNIQUE (ClientId, AgentId)
);