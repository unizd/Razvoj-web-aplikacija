import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { PortfolioModel } from './models/portfolio-model';
import { ContactModel } from './models/contact-model';
import { AboutModel } from './models/about-model';

let httpOptions = {
	headers: new HttpHeaders({
		'Content-Type': 'application/json'
	})
};

@Injectable({
  providedIn: 'root'
})
export class ServiceService {
	
	private aboutUrl = '/api/v1/about';
	private portfolioUrl = '/api/v1/portfolio';
	private contactUrl = '/api/v1/contact';

	constructor(private http: HttpClient) {
		
	}
	
	getAbout(): Observable<AboutModel> {
		return this.http.get<AboutModel>(this.aboutUrl, httpOptions)
			.pipe(
					tap(_ => console.log('Fetched about data')),
					catchError(this.handleError('getAbout', new AboutModel()))
				);
    }
	
	getPortfolio(): Observable<PortfolioModel[]> {
		return this.http.get<PortfolioModel[]>(this.portfolioUrl, httpOptions)
			.pipe(
					tap(_ => console.log('Fetched portfolio data')),
					catchError(this.handleError('getPortfolio', []))
				);
    }
	
	getContact(): Observable<ContactModel> {
		return this.http.get<ContactModel>(this.contactUrl, httpOptions)
			.pipe(
					tap(_ => console.log('Fetched contact data')),
					catchError(this.handleError('getContact', new ContactModel()))
				);
    }
	
	/**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
	handleError<T> (operation = 'operation', result?: T) {
		return (error: any): Observable<T> => {
			console.error(error);
			return of(result as T);
		};
	}
}
